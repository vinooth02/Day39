class FileReader:

    def read_file(self, filename):

        try:
            with open(filename, "r") as file:
                return file.read()

        except FileNotFoundError:
            return "File not found"