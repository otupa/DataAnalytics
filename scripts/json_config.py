from os.path import dirname, realpath, isfile, join
import json
from json import load, dump

class ConfigJson():
    def __init__(self):
        self.path = dirname(realpath(__file__))
        self.archive = join(self.path, 'config.txt')
        try:
            with open(self.archive, 'r') as file:
                self.data = load(file)
        except:
            self.data = {}
            self.base_config()

    def save_config(self):
        with open(self.archive, 'w') as file:
            dump(self.data, file, indent=3)

    def base_config(self):
        self.data["values"] = {"common":{}, "special":{}}
        self.data["values"]["common"] = {"normal":{}, "desc":{}}
        self.data["values"]["special"] = {"normal":{}, "desc":{}}
        self.data["records"] = {}
        self.save_config()

    def mod_records(self, name, porcent):
        self.data["records"][name] = {}
        self.data["records"][name]["porcent"] = porcent
        self.save_config()

    def mod_values(self, argument):
        self.data["values"]["common"]["normal"] = argument[0][0]
        self.data["values"]["common"]["desc"] = argument[0][1]
        self.data["values"]["special"]["normal"] = argument[1][0]
        self.data["values"]["special"]["desc"] = argument[1][1]
        self.save_config()

    def del_record(self, name):
        del self.data["records"][name]
        self.save_config()

    def mod_record_list(self, argument):
        for item in argument:
            if not self.data["records"][item]:
                self.mod_records(item, 0)
        self.save_config()

    def get_records(self):
        return [(item, value["value"]) 
            for item, value in self.data["records"].items()]

    def get_value(self):
        return self.data["values"]
    
    


if __name__ == '__main__':
    porcents = [
        [{"10":10, "12":15, "20":20}, {"10":-90, "12":-85, "20":-80}],
        [{"10":10, "12":15, "20":20}, {"10":-90, "12":-85, "20":-80}]
    ]

    config = ConfigJson()

    # config.mod_values(porcents)

    # print(config.get_json_records())
    # print(config.get_json_value())

    # def porcents(self):
    #     return (0.10, -0.90, 0.15, -0.85, 0.20, -0.80)