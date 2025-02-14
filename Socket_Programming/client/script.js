import { io } from "socket.io-client"

const joinRoomButton = document.getElementById("room-button")
const messageInput = document.getElementById("message-input")
const roomInput = document.getElementById("room-input")
const form = document.getElementById("form")

const socket = io('http://127.0.0.1:3000')
socket.on('connect', () =>{
    displaMessage(`connected to the server with id ${socket.id}`)
})

socket.on('receive-message', message => {
    displaMessage(message)
})

form.addEventListener("submit", e=>{
    e.preventDefault()
    const message = messageInput.value
    const room = roomInput.value

    if (message === "") return
    displaMessage(message)
    socket.emit('send-message', message, room)
    messageInput.value = ""
})
joinRoomButton.addEventListener("click", () =>{
    const room = roomInput.value
    socket.emit('join-room', room, message => {
        displaMessage(message)
    })
})

function displaMessage(message) {
    const div = document.createElement("div")
        div.textContent = message
        document.getElementById("message-container").append(div)
}