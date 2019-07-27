# importing modules
import json
import io
import os

# datamodel class with initializers for the 3 variables
class DataModel:
    def __init__(self, name, date, time):
        self.name = name
        self.time = time
        self.desc = desc

    # creates a JSON structure with the parameters provided, ie. existing array and/or the 3 variables
    def createJson(reminders, name, time, desc):
        if reminders is None:
            data = []
            data.append ({
                'name': name,
                'time': time,
                'desc': desc
            })
        else:
            reminders.append([name, time, desc])
            data = [len(reminders)]
            for reminder in reminders:
                content = {'name': reminder[0], 'time': reminder[1], 'desc': reminder[2]}
                data.append(content)
        with open('reminders.json', 'w') as json_file:
            json.dump(data, json_file)

    # checks if JSON file exists at the project file path
    def checkfile():
        return os.path.exists('reminders.json')

    # uses function above to check json file created or not, then reads if it exists,
    # and stores the data read to an array of dictionaries
    def readJson():
        dataArray = []
        if DataModel.checkfile():
            with open('reminders.json', 'r') as json_file:
                data = json.load(json_file)
                jsoncontent = "Json content: {}".format(data)
                if len(data)is 1:
                    for x in data:
                        if (x["name"] is not None) & (x["time"] is not None) & (x["desc"] is not None):
                            name = x['name']
                            time = x['time']
                            desc = x['desc']
                            dataArray.append([name, time, desc])
                            return dataArray

                elif len(data)>=2:
                    for index in data[1:]:
                        name = index['name']
                        time = index['time']
                        desc = index['desc']
                        dataArray.append([name, time, desc])
                        contents = "dataArray: {}".format(dataArray)
                    return dataArray

                else:
                    return nil
        else:
            createJson(name, time, desc)

    # removes the dictionary present at index of the data array
    def modifyJson(index):
        data = DataModel.readJson()
        data.pop(index-1)
        return data

    # uses the array provided to update the json file
    def updateDeletedJson(reminders):
        data = [len(reminders)]
        for reminder in reminders:
            content = {'name': reminder[0], 'time': reminder[1], 'desc': reminder[2]}
            data.append(content)
        with open('reminders.json', 'w') as json_file:
            json.dump(data, json_file)