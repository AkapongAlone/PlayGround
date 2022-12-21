import { TableContainer, Paper, Table, TableHead, TableRow, TableCell, TableBody } from "@mui/material";


function createData(
    name: string,
    skill: string,
    match: number,
    mustPay: number,
    
  ) {
    return { name, skill, match, mustPay };
  }
  
  const rows = [
    createData('Frozen yoghurt', "P-", 6.0, 24,),
    createData('Ice cream sandwich', "P-", 9.0, 37,),
    createData('Eclair', "P-", 16.0, 24,),
    createData('Cupcake', "P-", 3.7, 67,),
    createData('Gingerbread', "P-", 16.0, 49),
  ];


const Main = () => {
    return (
    <div className= "container mx-auto p-5">
    <TableContainer  component={Paper}>
      <Table  sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Name</TableCell>
            <TableCell align="right">Skill</TableCell>
            <TableCell align="right">Number of Match</TableCell>
            <TableCell align="right">Cost&nbsp;(bath)</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="right">{row.skill}</TableCell>
              <TableCell align="right">{row.match}</TableCell>
              <TableCell align="right">{row.mustPay}</TableCell>
             
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
    </div>
    )
}

export default Main