import os


print('Validation !')

input('Start  : (Any key)')

result = ''
for n in range(1, 6):
    i = 10 * (10 ** n)

    if n < 4:
        upload = os.path.join(str(n), 'to_upload')
        download = os.path.join(str(n), 'to_download')
        amount_u = len(os.listdir(upload))
        amount_d = len(os.listdir(download))

    else:
        amount_u = 0
        amount_d = 0

        sub_dir = 10 ** (5 - n)
        for i in range(sub_dir):
            i += 1
            upload = os.path.join(str(n), 'to_upload')
            download = os.path.join(str(n), 'to_download')
            amount_u += len(os.listdir(upload))
            amount_d += len(os.listdir(download))


    print(f'-------{n}-------')
    result += f'-------{n}-------\n'
    if i != amount_u:
        print(f'Check [to_upload] if all upload files are in {n} file')
        result += f'Check [to_upload] if all upload files are in {n} file\n\n'
        continue

    print(f'Upload files : {amount_u}\nDownload files : {amount_d}')
    print(f'Rate of Lossless : {amount_d / amount_u}\n')

    result += f'Upload files : {amount_u}\nDownload files : {amount_d}\n'
    result += f'Rate of Lossless : {amount_d / amount_u}\n\n'

with open('Result.txt', 'w') as f:
    f.write(result)

input('')
input('End  : (Any key)')
