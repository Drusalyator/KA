"""Модуль реализующий логику программы"""


class Solver:
    """Класс лабиринта"""

    def __init__(self):
        self._read_data_from_file()

    def _read_data_from_file(self):
        """Чтение данных лаюиринта из файла"""
        with open('in.txt') as file:
            self.number_of_rows = int(file.readline().strip())
            self.number_of_columns = int(file.readline().strip())
            self.labyrinth = []
            for row in range(self.number_of_rows):
                self.labyrinth.append([])
                line = file.readline()
                for char in line:
                    if char != ' ' and char != '\n':
                        self.labyrinth[row].append(int(char))
            self.start_coordinates = self._read_coordinate(file)
            self.end_coordinates = self._read_coordinate(file)
            self.come_from = {}

    @staticmethod
    def _read_coordinate(file):
        """Чтение координат начального и конечного положений"""
        temp_array = []
        for element in file.readline().strip().split(' '):
            if element == ' ' or element == '':
                continue
            else:
                temp_array.append(int(element) - 1)
        return tuple(temp_array)

    def get_item(self, x, y):
        """Получение элемента лабиринта по координатам"""
        return self.labyrinth[x][y]

    def find_way(self):
        """Найти путь между двумя клетками (обход в ширину)"""
        queue = []
        visited_cells = []
        if self.get_item(*self.end_coordinates) == 1 or self.get_item(*self.start_coordinates) == 1:
            return False
        queue.append(self.start_coordinates)
        while len(queue) != 0:
            coordinates = queue.pop(0)
            if coordinates == self.end_coordinates:
                return True
            visited_cells.append(coordinates)
            for dx in [0, -1, 1]:
                for dy in [-1, 0, 1]:
                    if coordinates[0] + dx < 0 or coordinates[1] + dy < 0 \
                            or coordinates[0] + dx >= self.number_of_rows or coordinates[1] >= self.number_of_columns:
                        continue
                    if (dx != 0 and dy != 0) or (coordinates[0] + dx, coordinates[1] + dy) in visited_cells \
                            or self.get_item(coordinates[0] + dx, coordinates[1] + dy) == 1:
                        continue
                    else:
                        queue.append((coordinates[0] + dx, coordinates[1] + dy))
                        self.come_from.update({(coordinates[0] + dx, coordinates[1] + dy): coordinates})
        return False

    def restore_path(self):
        """Восстаноление пути до конечной точки и запись в файл"""
        with open('out.txt', 'w') as file:
            if self.find_way():
                restore_path = []
                coordinates = self.end_coordinates
                while coordinates != self.start_coordinates:
                    restore_path.append((coordinates[0] + 1, coordinates[1] + 1))
                    coordinates = self.come_from[coordinates]
                restore_path.append((coordinates[0] + 1, coordinates[1] + 1))
                restore_path.reverse()
                file.write('Y\n')
                for coordinates in restore_path:
                    file.write(f'{coordinates[0]} {coordinates[1]}\n')
            else:
                file.write('N')


def main():
    """Точка входа"""
    try:
        labyrinth_solver = Solver()
        labyrinth_solver.restore_path()
        print('Complete')
    except Exception as e:
        print('Error: {}'.format(e))


if __name__ == '__main__':
    main()
