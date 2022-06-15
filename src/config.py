import configparser


# Add the structure to the file we will create

def definecfgFile():
    config = configparser.ConfigParser()
    config.add_section('user_info')
    config.set('user_info', 'Mitglied', '')
    config.set('user_info', 'user_role', '')
    config.set('user_info', 'user_profession', '')
    config.set('user_info', 'user_id', '')

    config.add_section('database-connection')
    config.set('database-connection', 'host', '')

    config.add_section('used_data')
    config.set('used_data', 'last_files', '')

    # Write the new structure to the new file
    with open(r"/Users/Shared/PycharmProjects/arvensteynIII/configfile.ini", 'w') as configfile:
        config.write(configfile)



def Anmeldung(ID, Kopfzeile, Role, Profession):
    edit = configparser.ConfigParser()
    edit.read("/Users/Shared/PycharmProjects/arvensteynIII/configfile.ini")

    ID = str(ID)

    # Get the userinfo section
    Benutzerinfo = edit["user_info"]
    # Update the password
    Benutzerinfo["Mitglied"] = Kopfzeile
    Benutzerinfo["user_role"] = Role
    Benutzerinfo["user_profession"] = Profession
    Benutzerinfo["user_id"] = ID

    if not Benutzerinfo == '':
        with open('/Users/Shared/PycharmProjects/arvensteynIII/configfile.ini', 'w') as configfile:
            edit.write(configfile)
    else:
        pass
    currentConfig.getcurrent_ra(self=currentConfig)


class currentConfig():
    def __init__(self):
        self.content = configparser.ConfigParser()
        self.content.read("/Users/Shared/PycharmProjects/arvensteynIII/configfile.ini")

        self.user_info = self.content["user_info"]
        self.Name = self.user_info["Mitglied"]
        self.Beruf = self.user_info["user_profession"]
        self.user_id = self.user_info["user_id"]

    def getcurrentfiles(self):
        self.content = configparser.ConfigParser()
        self.content.read("/Users/Shared/PycharmProjects/arvensteynIII/configfile.ini")

        self.lastFiles = self.content["used_data"]
        self.list_of_files = self.lastFiles["last_files"]
        self.list_of_files = [str(x) for x in self.list_of_files.split(",")]
        return self.list_of_files

    def getcurrent_ra(self):
        self.content = configparser.ConfigParser()
        self.content.read("/Users/Shared/PycharmProjects/arvensteynIII/configfile.ini")

        self.user_info = self.content["user_info"]
        self.user_id = self.user_info["user_id"]

        if not self.user_id == '':
            self.user_id = int(self.user_id)
        else:
            self.user_id = 0
        return self.user_id

    def getcurrent_tier(self):
        self.content = configparser.ConfigParser()
        self.content.read("/Users/Shared/PycharmProjects/arvensteynIII/configfile.ini")

        self.user_info = self.content["user_info"]
        self.user_tier = self.user_info["user_role"]

        if not self.user_tier == '':
            self.user_id = str(self.user_tier)
        else:
            self.user_id = 'default'
        return self.user_tier









def last_files_update(most_current):
    edit = configparser.ConfigParser()
    edit.read("/Users/Shared/PycharmProjects/arvensteynIII/configfile.ini")

    LastFiles = edit["used_data"]
    if LastFiles["last_files"] == "":
        LastFiles["last_files"] = most_current
        with open('/Users/Shared/PycharmProjects/arvensteynIII/configfile.ini', 'w') as configfile:
            edit.write(configfile)
    else:
        print("no sweat")

    prev_list = LastFiles["last_files"]
    prev_list = [str(x) for x in prev_list.split(",")]

    if most_current in prev_list:
        print("Nothing new")
    else:
        if len(prev_list) >= 10:
            prev_list = prev_list[1:]
        else:
            pass
        prev_list.append(most_current)
        new_list = ','.join(prev_list)
        LastFiles["last_files"] = new_list

        with open('/Users/Shared/PycharmProjects/arvensteynIII/configfile.ini', 'w') as configfile:
            edit.write(configfile)

