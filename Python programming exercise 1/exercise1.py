import re

def countandreplace(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
        count = len(re.findall(r'\bterrible\b', data))
        print(f'The word "terrible" appears {count} times.')
        data = re.split(r'(\bterrible\b)', data)
        j = 0
        for i in range(len(data)):
            if data[i] == 'terrible':
                j = j + 1
                if j % 2 == 0:
                    data[i] = 'pathetic'
                else:
                    data[i] = 'marvellous'
        with open('result.txt', 'w') as f:
            f.write(''.join(data))
            print('New file written successfully')

countandreplace('file_to_read.txt')