DIR=$1
echo "It is working"

display_file(){
    FILES=$(ls -R $1)
    echo $FILES
    # for FILE in $FILES
    # do
    #     if [ -d $FILE ]
    #     then
    #         echo "It is Dir"
    #         display_file $FILE
    #     else
    #         echo "Filename $FILE inside $1"
    #     fi
    # done
}

display_file $DIR
