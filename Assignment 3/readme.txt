ReadMeFirst:
1. I implement the "Apriori Algorithm" in Python, to run my code:
    --> Go to the directory of my ".py" files
    --> Copy this command "python {Name}.py -f {PathToFile} -s 0.01  -c 0"
    --> Note that replace the {Name with 1 of 3 names}
    --> I give relative_min_support as 0.01 for the command
    --> The second param is min_confidence, just leave it to be 0 because we don't consider it for Step 1

    --> To change the name of the output text file, you need to open my ".py" in any code editor and go to the function "writeFile" to modify a little bit

2. The output text  is in the same format as the sample.txt
3. For the frequent patterns with the same support, they have no order and for the items in the same frequent pattern, they are not ordered either.
    Because for these 2 cases, the order does not matter much.

4. The running time of my code is about 7s for topic-i on average
5. q1 is for frequent patterns
   q2 is for closed patterns
   q3 is for max patterns