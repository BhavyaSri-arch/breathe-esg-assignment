import { useEffect, useState } from 'react'
import axios from 'axios';

function App() {

  const [records, setRecords] = useState([])
  const [file, setFile] = useState(null)

  const fetchRecords = async () => {

    const res = await axios.get(
      'https://breathe-esg-assignment-production.up.railway.app'
    )

    setRecords(res.data)
  }

  useEffect(() => {
    fetchRecords()
  }, [])

  const uploadFile = async () => {

    const formData = new FormData()

    formData.append('file', file)

    await axios.post(
      'http://127.0.0.1:8000/api/upload/sap/',
      formData
    )

    fetchRecords()
  }

  const approveRecord = async (id) => {

    await axios.post(
      `http://127.0.0.1:8000/api/records/${id}/approve/`
    )

    fetchRecords()
  }

  return (

    <div style={{ padding: '40px' }}>

      <h1>ESG Review Dashboard</h1>

      <br />

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={uploadFile}>
        Upload SAP CSV
      </button>

      <br />
      <br />

      <table border="1" cellPadding="10">

        <thead>

          <tr>
            <th>ID</th>
            <th>Category</th>
            <th>Scope</th>
            <th>Quantity</th>
            <th>Status</th>
            <th>Suspicious</th>
            <th>Action</th>
          </tr>

        </thead>

        <tbody>

          {records.map((record) => (

            <tr key={record.id}>

              <td>{record.id}</td>

              <td>{record.category}</td>

              <td>{record.scope}</td>

              <td>{record.quantity}</td>

              <td>{record.status}</td>

              <td>
                {record.suspicious ? '⚠️ Yes' : 'No'}
              </td>

              <td>

                <button
                  onClick={() => approveRecord(record.id)}
                >
                  Approve
                </button>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  )
}

export default App