const computerChoiceDisplay=document.getElementById("computer-choice")
const usserChoiceDisplay=document.getElementById("user-choice")
const resultChoice=document.getElementById("result")
const possibleChoice=document.querySelectorAll('button')
let usserChoice
let computerChoice
let result
possibleChoice.forEach(possibleChoices => possibleChoices.addEventListener('click',(e)=>{
    usserChoice=e.target.id
    usserChoiceDisplay.innerHTML=usserChoice
    genrateComputerChoice()
    getResult()
    

}))


function genrateComputerChoice(){
    const randomNumber=Math.floor(Math.random() * 3)+1  //or u can use usserChoice.lenght
    //console.log(randomNumber)
    if(randomNumber===1){
        computerChoice='ROCK'
    }
    if(randomNumber===2){
        computerChoice='PAPER'
    }
    if(randomNumber===3){
        computerChoice='SECISSORS'
    }
    computerChoiceDisplay.innerHTML=computerChoice
}
function getResult(){
    if(computerChoice===usserChoice){
        result='IT IS A DRAW'

    }
    if(computerChoice==='ROCK' && usserChoice==='PAPER'){
        result='YOU WIN'
        
    }
    if(computerChoice==='ROCK' && usserChoice==='SECISSORS'){
        result='YOU LOST'
        
    }
    if(computerChoice==='PAPER' && usserChoice==='SECISSORS'){
        result='YOU WIN'
        
    }
    if(computerChoice==='PAPER' && usserChoice==='ROCK'){
        result='YOU LOST'
        
    }
    if(computerChoice==='SECISSORS' && usserChoice==='ROCK'){
        result='YOU WIN'
        
    }
    if(computerChoice==='SECISSORS' && usserChoice==='PAPER'){
        result='YOU LOST'
        
    }
    resultChoice.innerHTML=result
    console.log(result)
    
    
}


