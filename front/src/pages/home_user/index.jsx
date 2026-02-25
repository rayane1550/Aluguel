import React, { useEffect, useState } from "react"
import axios from "axios"
import './styles.css'

export default function HomeUser() {
    const [user, setUser] = useState([])
    const [password, setPassword] = useState('')

    const token = localStorage.getItem('token')

    const listar = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/usuarios', {
                headers: { Authorization: `Bearer ${token}` }
            })
            // console.log("Lista de usuários: ", response.data); 
            setUser(response.data)

        } catch (error) {
            console.log(error);
        }
    }

    useEffect(() => { listar() }, [])

    return (
        <div>
            <div className="Buscar_usuario">
                <h2>Buscar Usuario</h2>
                <input
                    className="Buscar"
                    value={usuario}
                    onChange={(e) => { setUsuario(e.target.value) }}
                    placeholder="Buscar Usuario"
                />
            </div>
            <div>
                <h2>Lista de Usuários</h2>
                {/*Tabela principal */}
                <table border="1" cellPadding="6" style={{ width: "100%" }}>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nome</th>
                            <th>Email</th>
                            <th>Telefone</th>
                            <th>Tipo</th>
                        </tr>
                    </thead>
                    <tbody>
                        {user.map((u) => (
                            <tr key={u.id}>
                                <td>{u.id}</td>
                                <td>{u.nome}</td>
                                <td>{u.email}</td>
                                <td>{u.telefone}</td>
                                <td>{u.tipo}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
                <hr style={{ margin: "20px 0" }} />
            </div>
        </div>
    )
}

