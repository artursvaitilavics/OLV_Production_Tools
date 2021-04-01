class SuffixPrefixUpdate():

    def seperate_name_from_number(self, name):
        number = name.split('.')
        return number


    def fix_suffix(self, name):

        start = name.rfind('_')
        end = name.rfind(name[-1])
        print("END INDEX:", end)
        new_word = ''
        if len(name) > end:
            new_word = name[0: start:] + name[end + 1::]

        suffix = ''
        suffix_start = name.index(name[0])
        suffix_end = name.rfind('_')

        if len(name) > suffix_end:
            suffix = name[0: suffix_start] + name[suffix_end + 1::]

        split_suffix = suffix.split('.')
        number = ''
        if len(split_suffix) > 1:
            suffix = split_suffix[0]
            number = split_suffix[1]

        return {'name': new_word, 'suffix': suffix, 'number': number}


    def fix_prefix(self, name, new_prefix, old_prefix):
        name = name.replace(old_prefix ,new_prefix)
        return name

update = SuffixPrefixUpdate()

my_name = "geo_51Box_suffixAAA.001"

print(update.fix_prefix(my_name, 'mat', 'geo'))

