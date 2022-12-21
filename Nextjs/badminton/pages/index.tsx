import type { NextPage } from 'next'
import Header from './component/header'
import AddNew from './component/addNew'
import Main from './component/main'
import ResponsiveAppBar from './component/Bad_header'
import Gen from './component/genMatch'
const Home: NextPage = () => {
  return (
    <div className='bg-gradient-to-br from-black to-red-500 h-screen'> 
      {/* <Header/> */}
      <ResponsiveAppBar/>
      <Main/>
      <AddNew/> 
      <Gen/>
    </div>
    
  )
}

export default Home
