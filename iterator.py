class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration  # stop iteration 


myclass = MyNumbers()
myiter = iter(myclass)

# for num in myiter:
#     print(num)
# mytuple = 'strings'
# myiter = iter(mytuple)

#print(next(myiter))
# print(next(myiter))
