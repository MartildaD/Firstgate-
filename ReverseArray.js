
function reverseArray(array) {
    for(let index = 0; index < array.length; index++){
    let first = 0;
    let second = array[index].length - 1;
    
    while(first < second){
        let old = array[index][first];
            array[index][first] = array[index][second];
            array[index][second] = old;
            first++; second--;
}
}
    return array;
}

    let input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 


console.log(reverseArray(input));

