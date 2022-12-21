import * as React from 'react';
import Box from '@mui/material/Box';
import { TextField, FormControl, InputLabel, Select, MenuItem, Button } from '@mui/material';



const AddNew = () => {
    return (
        <div className='container-sm mx-auto flex items-center justify-center p-5'>
        <div className='bg-white text-center rounded-3xl shadow-xl p-10 '>
        <h1 className='self-center text-gray-500 text-xl font-semibold'>Add New Player</h1>
        <Box
        component="form"
        className=' flex flex-row flex-wrap items-center justify-center'
        sx={{
            p:2,
            m:1,
            
            background:"white",
             '& > :not(style)': { m: 1, width: '20ch' },
      }}
        noValidate
        autoComplete="off"
      >
        <TextField id="outlined-basic" label="Name" variant="outlined" />
        <FormControl >
        <InputLabel id="demo-simple-select-label">Skill</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          defaultValue={30}
          label="Age"
        //   onChange={handleChange}
        >
          <MenuItem value={10}>N</MenuItem>
          <MenuItem value={20}>S</MenuItem>
          <MenuItem value={30}>P-</MenuItem>
          <MenuItem value={40}>P/P+</MenuItem>
          <MenuItem value={50}>C</MenuItem>
        </Select>
      </FormControl>
      <Button
      sx={{color: 'error.main'}}
        className="border-solid  border-2 bg-pink-200"
        variant="outlined"
      >
        Add
      </Button>
      </Box>
      </div>
      </div>
    )
}

export default AddNew