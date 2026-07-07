mkdir project
touch project1.txt
cp project1.txt project2.txt
mv project1.txt project2.txt
find . -name "project2.txt"

chmod 755 script.sh
tar -cvf project.tar.gz project/
mkdir extracted
tar -cvf project1.tar.gz -C  extracted_project1
tree
