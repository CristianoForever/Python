print ("This program converts F to C")
import easygui
F = easygui.enterbox ("Please Enter F")
F = float (F)
C = (F - 32) * 5.0/ 9
C = str(C)
#print 'C equals', C
easygui.msgbox ("C equals" + C)
