grammar cfg17;
s : s1;
s1 : 'c' s2;
s2 : 'c' s3 | EOF;
s3 : 'c' s4 | EOF;
s4 : EOF;
