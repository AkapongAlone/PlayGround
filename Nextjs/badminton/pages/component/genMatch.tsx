import { TableContainer, Paper, Table, TableHead, TableRow, TableCell, TableBody, Button } from "@mui/material"

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
  ];


const Gen = () => {
    return (
        <div className= "container mx-auto p-5  ">
        <div className="flex ">
        <TableContainer className="mx-5"  component={Paper}>
      <Table aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell align="center">First Team</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="column">
                {row.name} 
              </TableCell>
              </TableRow>

          ))}
        </TableBody>
      </Table>
    </TableContainer>
    <TableContainer  component={Paper}>
      <Table aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell align="center">Secend Team</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="column">
                {row.name} 
              </TableCell>
              </TableRow>

          ))}
        </TableBody>
      </Table>
    </TableContainer>
    </div>
    <Button
      sx={{color: 'error.main'}}
        className="flex mx-auto mt-4 border-solid  border-2 bg-black"
        variant="outlined"
      >
        Generate Match
      </Button>
    </div>
    )
}


export default Gen
