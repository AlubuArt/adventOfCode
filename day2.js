
let list = [
    [[1, 4],["a"], ["bcaaade"]],
    [[1, 5],["b"], ["cdbefg"]],
    ]

document.getElementById('inputfile').addEventListener('change', function(){
    let fr = new FileReader();
    console.log(fr.readAsText(this.files[0]))
})



let times;
let char;
let password;
let passwordString;
let str;
let counter = 0;

function solve(list) {
    
    for (let i = 0; i < list.length; i++) {
        times = list[i][0]
        char = list[i][1]
        password = list[i][2].toString()
        passwordString = password.split("");

        for (let n = 0; n < passwordString.length; n++) {
                if(passwordString[n] == char) {
                    counter++   
                }     
        }

        if(counter >= times[0] && counter <= times[1]) {
            console.log("valid")
            counter = 0;
        } else {
            console.log("invalid")
            counter = 0;
        }

    }

}


solve(list)
