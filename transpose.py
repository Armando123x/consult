 def transpose(self,block):

        block=deepcopy(block)
        (x,y)=block.shape

        buff=[]

        for nn in range(x):

            fila=block[nn]

            buff.insert(0,fila.tolist())

        return numpy.array(buff)
