accuracy_file = open('/root/mlopsactivity3/accuracy.txt','r')
input_file = open('/root/mlopsactivity3/input.txt','r')
data_file = open('/root/mlopsactivity3/data.txt','r')



new_accuracy = float(accuracy_file.read()) 

data = data_file.read()
data = data.split('\n')
epochs = int(data[0])


inputs = input_file.read()
inputs = inputs.split('\n')


if( new_accuracy < 99 ):
    epochs = epochs + 1   


data_file.close()
input_file.close()

#input_file = open('/root/mlopsactivity3/input.txt','w')
#input_file.close()
input_file = open('/root/mlopsactivity3/input.txt','w')
input_file.write(str(epochs))
input_file.close()