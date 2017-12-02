class Rot:

    def rot13(self, string):

        result = {}
        encrypted = ''

        for c in string:
            order = ord(c)

            #lower case
            if order >= ord('a') and order <= ord('z'):
                if order > ord('m'):
                    order -= 13
                else:
                    order += 13

            #upper case
            if order >= ord('A') and order <= ord('Z'):
                if order > ord('M'):
                    order -= 13
                else:
                    order += 13

            encrypted += chr(order)

        result['result'] = encrypted
        print(encrypted)

        return result

    def rot26(self, string):

        result = {}
        encrypted = ''

        for c in string:
            order = ord(c)

            if (order >= ord('a') and order <= ord('z')) or (order >= ord('A') and order <= ord('Z')):
                order -= 26

            order += 26
            encrypted += chr(order)

        result['result'] = encrypted

        return result
