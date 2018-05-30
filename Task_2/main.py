"""Модуль, реализующий логику программы"""


class Solver:
    """Класс решателя"""

    def __init__(self):
        """Конструктор"""
        self._read_data_from_file()
        self.find_components()
        self.writing_result()

    def _read_data_from_file(self):
        """Чтение данных из файла"""
        with open("in.txt") as file:
            self.number_of_vertices = int(file.readline().strip())
            self.graph = []
            self.components = []
            for i in range(self.number_of_vertices):
                self.graph.append([])
            adjacency_list = file.readline().strip()
            counter = 0
            while adjacency_list:
                temp_list = adjacency_list.split(" ")
                for element in temp_list:
                    if element == " " or element == "" or element == "0":
                        continue
                    else:
                        self.graph[counter].append(int(element))
                counter += 1
                adjacency_list = file.readline().strip()

    def find_components(self):
        """Найти компоненты связности в графе (поиск в глубину)"""
        visited_vertices = []
        for i in range(self.number_of_vertices):
            if i + 1 in visited_vertices:
                continue
            stack = [i + 1]
            component = []
            while len(stack) != 0:
                number_of_vertex = stack.pop(len(stack) - 1)
                vertices = self.graph[number_of_vertex - 1]
                visited_vertices.append(number_of_vertex)
                component.append(number_of_vertex)
                for vertex in vertices:
                    if vertex in visited_vertices or vertex in stack:
                        continue
                    stack.append(vertex)
            self.components.append(sorted(component))
        self.components.sort(key=lambda x: min(x))

    def writing_result(self):
        """Запись реультатов в файл"""
        with open("out.txt", "w") as file:
            result = ""
            result += f"{len(self.components)}\n"
            for component in self.components:
                for vertex in component:
                    result += f"{vertex} "
                result += "0\n"
            file.write(result[:-1])


def main():
    """Точка входа"""
    try:
        Solver()
    except Exception as exception:
        print("Error: {}".format(exception))


if __name__ == "__main__":
    main()
