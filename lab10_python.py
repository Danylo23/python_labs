class day1=None    static_val = 'static!'

    def __init__(self, text_message='lets go and dring some coffee', author="Danylo", delivery_date=29, receiver="Yana",
                 phone="Samsung", time="19:30"):
        self.text_message = text_message
        self.author = author
        self.delivery_date = delivery_date
        self.receiver = receiver
        self.phone = phone
        self.__time = time

    def __del__(self):
        print('destructor')

    def MessageInfo(self):
        print('Повідомлення: ' + self.text_message + '\nАвтор: ' + str(self.author) + '\nДата відправки: ' + str(
            self.delivery_date) +
              '\nОтримувач: ' + str(self.receiver) + '\nТелефон: ' + self.phone + '\nЧас: ' + str(self.__time) + '\n')

    @staticmethod
    def get_static_val(self):
        return self.static_val

    @staticmethod
    def __sum__(x, y):
        return x + y


    def __fromBirthYear__(self, name):
        return self.name
