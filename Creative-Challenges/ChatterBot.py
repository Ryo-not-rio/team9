from random import randint

def InterpretFileContents(FileName):
    """
    File contents will be of form
    Input1:1stPossibleResponse;2ndPossibleResponse;3rdPossibleResponse;etc...
    Input2:1stPossibleResponse;2ndPossibleResponse;3rdPossibleResponse;etc...
    """

    OutputDict = {}
    ExitPhrases = []
    with open(FileName, "r") as ResponseFile:
        FileContents = ResponseFile.readlines()
        for Line in FileContents:
            if Line != FileContents[0]:
                Line = Line.replace("\n", "")
                KeyString = Line.split(":")[0]
                ValueList = Line.split(":")[1].split(";")
                OutputDict[KeyString] = ValueList
            else:
                ExitPhrases.extend(Line.split(";"))
    
    return OutputDict, ExitPhrases

def AppendToFile(FileName, InputString, OutputLst):
    with open(FileName, "a") as ResponseFile:
        TextToWrite = InputString + ":"
        for Output in OutputLst:
            TextToWrite += Output
            if Output != OutputLst[-1]:
                TextToWrite += ";"
            else:
                TextToWrite += "\n"
        ResponseFile.write(TextToWrite)

def Treat(String):
    NewString = String.lower().replace("?", "").replace("!", "").replace(",", "").replace(".", "").replace("(", "").replace(")", "")
    return NewString

if __name__ == "__main__":
    FileName = "Creative-Challenges/Responses.txt"
    ResponseDict, GoodbyePhrases = InterpretFileContents(FileName)
    ConvEnded = False
    while ConvEnded == False:
        UserInput = input("> ")
        UserInput = Treat(UserInput)
        if UserInput in GoodbyePhrases:
            ConvEnded = True
            print("Goodbye")
        else:
            Found = True
            for PossInput in ResponseDict.keys():
                if UserInput == PossInput:
                    Output = ResponseDict[PossInput][randint(0, len(ResponseDict) - 1)]
                    print(Output)
                elif PossInput in UserInput:
                    Output = ResponseDict[PossInput][randint(0, len(ResponseDict) - 1)]
                    print(Output)
            if Found == False:
                ## No response found
                NewResponseList = []
                MoreResponses = False
                while len(NewResponseList) == 0 or MoreResponses == True:
                    MoreResponses = False
                    NewResponseList.append(input("How should I answer that?\n> "))

                    if input("Are there more responses to that phrase?\n> ").lower()[0] == "y":
                        MoreResponses = True
                
                print("\n")
                AppendToFile(FileName, UserInput, NewResponseList)
                ResponsesDict = InterpretFileContents(FileName)