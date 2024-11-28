grammar cfg;
s : s3;
s1 : 'a' s3;
s3 : 'b' | 'c' | EOF | s1 s3;
