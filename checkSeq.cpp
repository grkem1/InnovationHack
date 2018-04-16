#include <iostream>
#include <string>

const int windowLength = 5;
const int threshold = 3;

using namespace std;


string checkSeq(string detections){
    string output;
    char signal;
    int i = 0;
    int level = 0;

    for (; i < windowLength; ++i){
        signal = detections[i];
        if(signal == 'Y'){
            level++;
        }
    }
    i--;
    if(level >= threshold){
        output.push_back('Y');
    }else{
        output.push_back('N');
    }
    i++;

    for (; i < detections.size(); ++i) {
        signal = detections[i];
        if(signal == 'Y'){
            level++;
        }
        if(detections[i - windowLength] == 'Y'){
            level--;
        }
        if(level >= threshold){
            output.push_back('Y');
        }else{
            output.push_back('N');
        }
    }

    return output;

}

int main(int argc, char *argv[]){

    string input = argv[1];
//    cout << input;
    cout << checkSeq(input);

}