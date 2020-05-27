accuracy_file = open('/root/mlopsactivity3/accuracy.txt','r')
input_file = open('/root/mlopsactivity3/input.txt','r')
data_file = open('/root/mlopsactivity3/data.txt','r')
#display_matter=open('root/mlopsactivity3/display_matter.html','r')


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
#display_matter=open('root/mlopsactivity3/displaymatter.html','w')

#display_matter.write('\nLayer -1')
#display_matter.write('\nNumber Of Filters : 20')
#display_matter.write('\nFilter Size : 5')
#display_matter.write('\nPool Size : 2')

#display_matter.write('\nLayer -2')
#display_matter.write('\nNumber Of Filters : 50')
#display_matter.write('\nFilter Size : 5')
#display_matter.write('\nPool Size : 2')
#display_matter.write('\nEpochs :'+ str(epochs))
#display_matter.close()

#display_matter = open('/mlopsactivity3.1/display_matter.html','r+')
#display_matter.read()
#display_matter.write('<pre>\n---------------------------------------------\n')
##display_matter.write(model.summary())

#display_matter.write('\nLayer -1')
#display_matter.write('\nNumber Of Filters : 20')
#display_matter.write('\nFilter Size : 5')
#display_matter.write('\nPool Size : 2')

#display_matter.write('\nLayer -2')
#display_matter.write('\nNumber Of Filters : 50')
#display_matter.write('\nFilter Size : 5')
#display_matter.write('\nPool Size : 2')
#display_matter.write('\nEpochs :'+ str(epochs))


#display_matter.write('\nAccuracy achieved : ' + str(scores[1])+'\n</pre>')
#display_matter.close()



