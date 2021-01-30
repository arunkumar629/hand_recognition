import os
for name in ['training']:
    with open('hand_dataset_{}.csv'.format(name), 'w') as output_file:
        print('=== creating {} dataset ==='.format(name))
        output_file.write('image_path,label\n')
        for i in range(4):
            path = '{}\{}'.format(name, i)
            for file in os.listdir(path):
                if file.endswith(".jpg"):
                    output_file.write('{},{}\n'.format(os.path.join(path, file), str(i)))