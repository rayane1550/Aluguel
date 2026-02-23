import axios from "axios"
import { useEffect } from "react";

export default function HomeUser() {
    const token = localStorage.getItem('token')

    const listar = async ()=>{
        const response = await axios.get('http://localhost:8000/api/usuarios')
        console.log("lista de usuarios: ", response.data);
    }
}

useEffect(()=>{listar()}, {})

return (
    <div>
        <p>Essa é a pagina Home User</p>
    </div>
)
