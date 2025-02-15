import { Server } from "socket.io";
import { instrument } from "@socket.io/admin-ui";
const io = new Server(3000, {
    cors: {
        origin: ["http://localhost:3000","http://localhost:5173", "https://admin.socket.io"],
        credentials: true
    }
});

io.on('connection', socket => {
    console.log(socket.id);
    socket.on('send-message', (message, room) => {
        if (room === "") {
            socket.broadcast.emit('receive-message', message)
        } else {
            socket.to(room).emit('receive-message', message)
        }
    })

    socket.on('join-room', (room, ch) => {
        socket.join(room)
        ch(`Joined room ${room}`)
    })
});

instrument(io, { 
    namespaceName: "/admin",
    auth: false 
});