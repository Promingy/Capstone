import { Route, createBrowserRouter, createRoutesFromElements } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import Redirect from '../components/Redirect'
import MainPage from '../components/MainPage';
import SelectedRecipe from '../components/SelectedRecipe'

export const router = createBrowserRouter(
  createRoutesFromElements(
    <Route element={<Layout />} >
      <Route path='/' element={<h1>Welcome!</h1>} />
      <Route path='/login' element={<LoginFormPage />} />
      <Route path='/signup' element={<SignupFormPage />} />
      <Route path='/main' element={<MainPage />} />
      <Route path='/recipes/:recipeId' element={<SelectedRecipe />} />
      <Route path='*' element={<Redirect />} />
    </Route>
  )
)
