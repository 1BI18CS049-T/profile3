print "the solution for "
print "in order to reach the top of tower,a monkey in hisfirst atempt reaches to aheight of 5 feet and in the subsequent jump,"
print "he slips by 2% of height attained in perious jump.the process takesrepeately until it reach toop,calculate number of attempts the monkey to reach top"
h=input('enter the height')
count=0
a=h
while h>0:
    h=h-5+0.2*5
    count=count+1
print 'number of attempts the monkey to reach top of height',a,":",count

