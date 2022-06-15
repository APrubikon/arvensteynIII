#packet = {"name_prefix": self.name_prefix, "name_first": self.name_first, "name_last": self.name_last,
#          "birthday": self.birthday, "organization": self.organization, "title": self.title, "role": self.role,
#          "work_address1": self.work_address_1, "work_city1": self.work_city_1, "work_zip1": self.work_zip_1,
#          "work_phone_1": self.work_phone_1, "work_phone_2": self.work_phone_2, "work_phone_3": self.work_phone_3,
#          "work_fax": self.work_fax_1, "mobile_phone_1": self.mobile_phone_1, "work_email_1": self.work_email_1,
#          "note": self.note, "url": self.url}
#
list = ['name_prefix', 'name_first', 'name_last', 'birthday', 'organization', 'title', 'role',
        'work_address1', 'work_city1', 'work_zip1', 'work_phone_1', 'work_phone_2', 'work_phone_3',
        'work_fax', 'mobile_phone_1', 'work_email_1', 'note', 'url', 'gesV', 'mandantID']
#new_human = self.record()
for i in list:
    print(f"""( , {i})""")