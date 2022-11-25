import CFGtoCNF
import codeTokenizer as ctok
import cyk
import sys

# # Get CNF Grammar
# CFGtoCNF.Converter()

# Load Chomsky Normal Form
if len(sys.argv) > 1:
    inputJs = str(sys.argv[1])
else:
	print("Must be 2 arument!")


cyk.LoadCNF("./Grammar/CNF.txt")

# Tokenize
tokenizedCode = ctok.tokenizeInput(inputJs)
print(tokenizedCode)

# CYK

table = cyk.cyk(tokenizedCode)

print("========================================================")
for x in table:
    print(x)

if (cyk.checkValidity(table, "SS")):
    print("Verdict accepted! Compile success!")
else:
    print("Compile error, wrong syntax!")