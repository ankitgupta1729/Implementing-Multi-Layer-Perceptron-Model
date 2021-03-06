#!/usr/bin/env python
# coding: utf-8

# In[429]:


# Importing Libraries
import numpy as np
import pandas as pd


# In[430]:


#reading .csv file and storing it in "dataset" dataframe
dataset=pd.read_csv("/home/ankit/Desktop/Iris.csv")


# In[431]:


print(dataset.head()) # printing the whole dataset
print(dataset['Species'].unique()) # printing the unique classes of iris dataset


# In[432]:


print(dataset.shape) # size of the dataset


# In[433]:


#X= dataset.drop('Species',axis=1)
#Y= dataset['Species']


# In[434]:


#print(X)


# In[435]:


#print(Y)


# In[436]:


data = dataset.to_numpy() # storing iris dataset as numpy array


# In[437]:


for i in range(150):
    data[i][0]=1 # adding 1st column as bias=1
    


# In[438]:


print(data)


# In[439]:


from matplotlib import pyplot as plt


for i in range(len(data)):
    if data[i][-1]=='Iris-setosa':
        data[i][-1]=1 # relabeling Iris setosa class as "0"
    if data[i][-1]=='Iris-versicolor':
        data[i][-1]=2 # relabeling Iris versicolor class as "1"
    if data[i][-1]=='Iris-virginica':
        data[i][-1]=3 # relabeling Iris virginica class as "0"
    data[i][0]=1 # initializing first column as 1 for bias    


# In[440]:


#data


# In[441]:


for i in range(len(data)):
    if data[i][-1]==1:
        plt.scatter(data[i,1],data[i,2],c='r')  
    if data[i][-1]==2:
        plt.scatter(data[i,1],data[i,2],c='g')      
    if data[i][-1]==3:
        plt.scatter(data[i,1],data[i,2],c='y')  
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')    
        
plt.show()    # a plot between sepal length and sepal width


# In[442]:


for i in range(len(data)):
    if data[i][-1]==1:
        plt.scatter(data[i,3],data[i,4],c='r')  
    if data[i][-1]==2:
        plt.scatter(data[i,3],data[i,4],c='g')      
    if data[i][-1]==3:
        plt.scatter(data[i,3],data[i,4],c='y')  
    plt.xlabel('petal length')
    plt.ylabel('petal width')    
        
plt.show()  # a plot between petal length and petal width


# ## Implementing Forward Propagation MLP for Iris dataset

# In[443]:


input_no_of_nodes = 4 # as features are 4-dimensional i.e. sepal length,petal length, sepal width 
# and petal width
no_of_hidden_layers = 1 # just for simplicity , I am taking one hidden layer with 4 nodes
no_of_classes = 3 # setosa,virginica and versicolor

# initializing input weights for output layer 

weight1 = [] # initializing weights


for k in range(3):
    w=[]
    for j in range(5):
        w.append(np.random.randn())
    weight1.append(w)    
        
print("input weight vector for output layer:\n ",weight1)

# initializing input weights for hidden layer 

weight2 = [] # initializing weights

bias= 1



for k in range(4):
    w=[]
    for j in range(5):
        w.append(np.random.randn())
    weight2.append(w)    
        
print("\ninput weight vector for hidden layer:\n ",weight2)


# In[444]:


#for dk(p), if class label belongs to class 1, we make 1st value as 1 and other values as 0. similarly for
#others

labels=[]
for i in range(150):
    if data[i][-1]==1:
        labels.append([1,0,0])
    if data[i][-1]==2:
        labels.append([0,1,0])
    if data[i][-1]==3:
        labels.append([0,0,1]) 


# In[445]:


forward_prop_output=[]

    # Input on input layer -1 (hidden layer )  by using McCullouch Pit model on input layer,
    
u1=[]
for j in range(4):
    sum=0
    for i in range(5):
        sum += weight2[j][i]*data[j][i]
    u1.append(sum)    
 #print("Input on layer 1 (hidden layer) : ",u)   
    
 # For output on layer 1, by using sigmoid function,

v1=[]
v1.append(1) # appending bias=1

for i in range(4):
    sig=1/(1+ np.exp(-u1[i]))
    v1.append(sig)
#print("output on layer 1 : ",v)    
    
    
# For input on layer 2 by using McCullouch Pit model,

u2=[]
for j in range(3):
    sum=0
    for i in range(5):
        sum += weight1[j][i]*v1[i]
    u2.append(sum)    
   #print("input of layer 2",u) 
    
    
# For output on layer 2(output layer), by using sigmoid function,

v2=[]

for i in range(3):
    sig=1/(1+ np.exp(-u2[i]))
    v2.append(sig)
   #print("output on layer 2 (output layer) : ",v)
forward_prop_output.append(v2)    
yk=forward_prop_output
    


# In[446]:


def forward_prop(p):
     forward_prop_output=[]

 # Input on input layer -1 (hidden layer )  by using McCullouch Pit model on input layer,
 
     u1=[]
     for j in range(4):
         sum=0
         for i in range(5):
             sum += weight2[j][i]*data[p][i]
         u1.append(sum)    
      #print("Input on layer 1 (hidden layer) : ",u)   
 
      # For output on layer 1, by using sigmoid function,

     v1=[]
     v1.append(1) # appending bias=1

     for i in range(4):
         sig=1/(1+ np.exp(-u1[i]))
         v1.append(sig)
     #print("output on layer 1 : ",v)    
 
 
     # For input on layer 2 by using McCullouch Pit model,

     u2=[]
     for j in range(3):
         sum=0
         for i in range(5):
             sum += weight1[j][i]*v1[i]
         u2.append(sum)    
        #print("input of layer 2",u) 
 
 
     # For output on layer 2(output layer), by using sigmoid function,

     v2=[]

     for i in range(3):
         sig=1/(1+ np.exp(-u2[i]))
         v2.append(sig)
        #print("output on layer 2 (output layer) : ",v)
     forward_prop_output.append(v2)    
     yk=forward_prop_output
 
     return yk


# In[447]:


#for dk(p), if class label belongs to class 1, we make 1st value as 1 and other values as 0. similarly for
#others

labels=[]
for i in range(150):
    if data[i][-1]==1:
        labels.append([1,0,0])
    if data[i][-1]==2:
        labels.append([0,1,0])
    if data[i][-1]==3:
        labels.append([0,0,1])    


# In[448]:


labels


# ## Implementing Backpropagation MLP for iris dataset

# In[449]:


def back_prop(p):
    # computing delta w_ji(0) (learning rule) #weight2

    learning_rate = 0.5 #assuming
    
    
    forward_prop_output=[]

    # Input on input layer -1 (hidden layer )  by using McCullouch Pit model on input layer,
    
    u1=[]
    for j in range(4):
        sum=0
        for i in range(5):
            sum += weight2[j][i]*data[p][i]
        u1.append(sum)    
        #print("Input on layer 1 (hidden layer) : ",u)   
    
        # For output on layer 1, by using sigmoid function,

    v1=[]
    v1.append(1) # appending bias=1

    for i in range(4):
        sig=1/(1+ np.exp(-u1[i]))
        v1.append(sig)
    #print("output on layer 1 : ",v)    
    
    
    # For input on layer 2 by using McCullouch Pit model,

    u2=[]
    for j in range(3):
        sum=0
        for i in range(5):
            sum += weight1[j][i]*v1[i]
        u2.append(sum)    
        #print("input of layer 2",u) 
    
    
    # For output on layer 2(output layer), by using sigmoid function,

    v2=[]

    for i in range(3):
        sig=1/(1+ np.exp(-u2[i]))
        v2.append(sig)
        #print("output on layer 2 (output layer) : ",v)
    forward_prop_output.append(v2)    
    yk=forward_prop_output
        
    
    
    
    for k in range(3):
        for j in range(5):
            delta_w_kj_1 = (labels[p][k] - yk[0][k])*(yk[0][k])*(1-yk[0][k])*v1[j]

    delta_w_kj_1=learning_rate*delta_w_kj_1            
    #print(delta_w_kj_1)
    
    
    # computing delta w_ji(0) (learning rule) #weight2

    learning_rate = 0.5 #assuming


    for k in range(3):
        for j in range(5):
            for l in range(5):
                delta_w_ji_0 = (labels[p][k] - yk[0][k])*yk[0][k]*(1-yk[0][k])*weight1[k][j]*v1[j]*(1-v1[j])*data[p][l]

    delta_w_ji_0=learning_rate*delta_w_ji_0                   
    #print(delta_w_ji_0)
    
    # modifying weight1 and weight2 according to delta_w
    #print("previous weight1 matrix : ", weight1)
    temp1=0
    for k in range(3):
        for j in range(5):
            temp1 =weight1[k][j]
            weight1[k][j] =temp1+delta_w_kj_1
        
        
    #print("modified input weight vector for output layer:\n ",weight1)
    
    #print("Previous weight2 matrix : ", weight2)

    temp2=0
    for k in range(4):
        for j in range(5):
            temp2=weight2[k][j]
            weight2[k][j] = temp2+ delta_w_ji_0
        
        
    #print("modified input weight vector for hidden layer:\n ",weight2)
    
    return
    


# In[450]:


error1=0
for p in range(150):
    output1=forward_prop(p)
    #print(output)
    for j in range(3):
        error1 += pow((labels[p][j] - output1[0][j]),2)
    E1 = error1/2
print(E1)    #error after forward propagation initially


# In[451]:


for n in range(50):# number of iterations
    error=0
    for i in range(150):
        output=forward_prop(i)
        #print(output)
        #error = 0
        for j in range(3):
            error += pow((labels[i][j] - output[0][j]),2)
        E = error/2
        #print(E)
        #if E<0.1:
         #   break            
        back_prop(i)
print("Minimized error after 100 iteration: ", E) # Our objective was to Minimize the error by learning rule delta_w in backpropagation        

# if error difference is not much then incearease the number of iteration because error gets change by weight matrix


# In[452]:


print("Final input weight matrix for hidden layer: \n",weight2)
print("\nFinal input weight matrix for output layer: \n",weight1)


# ## Incorporating momentum factor 

# In[423]:


gamma=0.9
mom1=0
mom2=0


# In[424]:


#Modifying little bit the definition of backpropagation for error learning

def back_prop(p,mom1,mom2):
    # computing delta w_ji(0) (learning rule) #weight2

    learning_rate = 0.5 #assuming
    
    forward_prop_output=[]

    # Input on input layer -1 (hidden layer )  by using McCullouch Pit model on input layer,
    
    u1=[]
    for j in range(4):
        sum=0
        for i in range(5):
            sum += weight2[j][i]*data[p][i]
        u1.append(sum)    
     #print("Input on layer 1 (hidden layer) : ",u)   
    
    # For output on layer 1, by using sigmoid function,

    v1=[]
    v1.append(1) # appending bias=1

    for i in range(4):
        sig=1/(1+ np.exp(-u1[i]))
        v1.append(sig)
    #print("output on layer 1 : ",v)    
    
    
    # For input on layer 2 by using McCullouch Pit model,

    u2=[]
    for j in range(3):
        sum=0
        for i in range(5):
            sum += weight1[j][i]*v1[i]
        u2.append(sum)    
        #print("input of layer 2",u) 
    
    
    # For output on layer 2(output layer), by using sigmoid function,

    v2=[]

    for i in range(3):
        sig=1/(1+ np.exp(-u2[i]))
        v2.append(sig)
        #print("output on layer 2 (output layer) : ",v)
    forward_prop_output.append(v2)    
    yk=forward_prop_output
        
    
    for k in range(3):
        for j in range(5):
            delta_w_kj_1 = (labels[p][k] - yk[0][k])*(yk[0][k])*(1-yk[0][k])*v1[j]

    delta_w_kj_1=learning_rate*delta_w_kj_1            
    #print(delta_w_kj_1)
    
    
    # computing delta w_ji(0) (learning rule) #weight2

    learning_rate = 0.5 #assuming


    for k in range(3):
        for j in range(5):
            for l in range(5):
                delta_w_ji_0 = (labels[p][k] - yk[0][k])*yk[0][k]*(1-yk[0][k])*weight1[k][j]*v1[j]*(1-v1[j])*data[p][l]

    delta_w_ji_0=learning_rate*delta_w_ji_0                   
    #print(delta_w_ji_0)
    
    # modifying weight1 and weight2 according to delta_w
    #print("previous weight1 matrix : ", weight1)
    
    # Here, I am using the concept of momentum factor
    mom1 += pow(gamma,i)*(delta_w_kj_1)
    mom2 += pow(gamma,i)*(delta_w_ji_0)       
    
    temp1=0
    for k in range(3):
        for j in range(5):
            temp1 =weight1[k][j]
            weight1[k][j] =temp1+(mom1 + delta_w_kj_1)
        
        
    #print("modified input weight vector for output layer:\n ",weight1)
    
    #print("Previous weight2 matrix : ", weight2)

    temp2=0
    for k in range(4):
        for j in range(5):
            temp2=weight2[k][j]
            weight2[k][j] = temp2+ (mom2 + delta_w_ji_0)
        
        
    #print("modified input weight vector for hidden layer:\n ",weight2)
    
    return mom1,mom2
    


# In[425]:


for n in range(100):# number of iterations
    error=0
    for i in range(150):
        output=forward_prop(i)
        #print(output)
        #error = 0
        for j in range(3):
            error += pow((labels[i][j] - output[0][j]),2)
        E = error/2
        #print(E)
        #if E<0.1:
         #   break  
                      
        back_prop(i,mom1,mom2)
        
print("Minimized error after 100 iteration: ", E) # Our objective was to Minimize the error by learning rule delta_w in backpropagation        

# if error difference is not much then incearease the number of iteration because error gets change by weight matrix


# In[ ]:




