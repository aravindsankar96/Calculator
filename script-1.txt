class Calculator {
    constructor(previousoperandTextelement, currentoperandTextelement) {
        this.previousoperandTextelement = previousoperandTextelement
        this.currentoperandTextelement = currentoperandTextelement
        this.clear()
    }

    clear() {
        this.previousoperand = ''
        this.currentoperand = ''
        this.operation = undefined
    }

    delete() {
        this.currentoperand = this.currentoperand.toString().slice(0, -1)
    }

    appendNumber(number) {
        if (number == '.' && this.currentoperand.includes('.')) return
        this.currentoperand = this.currentoperand.toString() + number.toString()
    }

    chooseOperation(operation) {
        if (this.currentoperand === '') return
        if (this.previousoperand !== '') {
            this.compute()
        }
        this.operation = operation
        this.previousoperand = this.currentoperand
        this.currentoperand = ''
    }

    compute() {
        let computation
        const prev = parseFloat(this.previousoperand)
        const curr = parseFloat(this.currentoperand)
        if (isNaN(prev) || isNaN(curr)) return
        switch (this.operation) {
            case '+':
                computation = prev + curr
                break
            case '-':
                computation = prev - curr
                break
            case 'x':
                computation = prev * curr
                break
            case '÷':
                computation = prev / curr
                break
            default:
                return
        }
        this.currentoperand = computation
        this.operation = undefined
        this.previousoperand = ''
    }


    getDisplayNumber(number) {
        const stringNumber = number.toString()
        const intergerDigits = parseFloat(stringNumber.split('.')[0])
        const decimalDigits = stringNumber.split('.')[1]
        let integerDisplay

        if (isNaN(intergerDigits)) {
            integerDisplay = ''
        } else {
            integerDisplay = intergerDigits.toLocaleString('en' , {
            maximumFractionDIgits: 0 })
        }
        if (decimalDigits != null) {
            return `${integerDisplay}.${decimalDigits}`
        } else {
            return integerDisplay
        }
    }

    updateDisplay() {
        this.currentoperandTextelement.innerText = this.getDisplayNumber(this.currentoperand)
        if(this.operation != null) {
        this.previousoperandTextelement.innerText = `${this.getDisplayNumber(this.previousoperand)} ${this.operation}`
        } else {
            this.previousoperandTextelement.innerText = ''
        }
    }
}

const numberButtons = document.querySelectorAll('[data-number]')
const operationButtons = document.querySelectorAll('[data-operation]')
const equalsButton = document.querySelector('[data-equals]')
const deleteButton = document.querySelector('[data-delete]')
const allclearButton = document.querySelector('[data-all-clear]')
const previousoperandTextelement = document.querySelector('[data-previous-operand]')
const currentoperandTextelement = document.querySelector('[data-current-operand]')

const calculator = new Calculator(previousoperandTextelement, currentoperandTextelement)
    numberButtons.forEach(button => {
        button.addEventListener('click', () => {
            calculator.appendNumber(button.innerText)
            calculator.updateDisplay()
        })
    })

    operationButtons.forEach(button => {
        button.addEventListener('click', () => {
            calculator.chooseOperation(button.innerText)
            calculator.updateDisplay()
        })
    })

    equalsButton.addEventListener('click', button => {
        calculator.compute()
        calculator.updateDisplay()
    })

    allclearButton.addEventListener('click', button => {
        calculator.clear()
        calculator.updateDisplay()
    })

    deleteButton.addEventListener('click', button => {
        calculator.delete()
        calculator.updateDisplay()
    })