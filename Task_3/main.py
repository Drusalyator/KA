"""Модуль реализующий логику программы и точку входа"""


class Solver:
    """Класс решателя"""

    def __init__(self):
        """Контруктор"""
        self._read_data_from_file()
        self._find_shortest_way()
        self.write_to_file()

    def _read_data_from_file(self):
        """Чтение данных из файла"""
        with open("in.txt") as file:
            self.count_of_vertices = int(file.readline().strip())
            self.nodes = set()
            self.distances = {}
            for i in range(self.count_of_vertices):
                self.nodes.add(i + 1)
            for m in self.nodes:
                self.distances.update({m: {}})
            for j in range(self.count_of_vertices):
                string = file.readline().strip()
                temp_list = string.split(" ")
                if temp_list[0] == "0":
                    continue
                distances = self._get_finish_arguments(temp_list)
                for k in range(0, len(distances), 2):
                    self.distances[j + 1].update({int(distances[k]): int(distances[k + 1])})
            self.start_vertex = int(file.readline().strip())
            self.end_vertex = int(file.readline().strip())

    @staticmethod
    def _get_finish_arguments(temp_list):
        """Получение массива дистанций"""
        finish_arguments = []
        for elements in temp_list:
            if elements == "" or elements == " ":
                continue
            finish_arguments.append(elements)
        finish_arguments.pop(len(finish_arguments) - 1)
        return finish_arguments

    def _find_shortest_way(self):
        """Поиск кратчайшего пути"""
        unvisited = {node: float("inf") for node in self.nodes}
        self.visited = {}
        self.parents = {}
        current = self.start_vertex
        current_distance = 0
        unvisited[current] = current_distance

        while True:
            for neighbour, distance in self.distances[current].items():
                if neighbour not in unvisited:
                    continue
                new_distance = current_distance + distance
                if unvisited[neighbour] is None or unvisited[neighbour] > new_distance:
                    unvisited[neighbour] = new_distance
                    self.parents.update({neighbour: current})
            self.visited[current] = current_distance
            del unvisited[current]
            if not unvisited:
                break
            candidates = [node for node in unvisited.items()]
            current, current_distance = sorted(candidates, key=lambda x: x[1])[0]

    def write_to_file(self):
        """Запись в файл"""
        with open("out.txt", "w") as file:
            result = ""
            if self.visited.get(self.end_vertex) == float("inf"):
                result += "N"
            else:
                result += "Y\n"
                way = []
                current = self.end_vertex
                while current != self.start_vertex:
                    way.append(current)
                    current = self.parents.get(current)
                way.append(self.start_vertex)
                way.reverse()
                for vertex in way:
                    result += f"{vertex} "
                result += f"\n{self.visited.get(self.end_vertex)}"
            file.write(result)


def main():
    """Точка входа"""
    try:
        Solver()
    except Exception as exception:
        print("Error: {}".format(exception))


if __name__ == '__main__':
    main()
