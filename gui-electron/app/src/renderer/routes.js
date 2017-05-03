export default [
  {
    path: '/',
    name: 'landing-page',
    component: require('components/Modularitea')
  },
  {
    path: '*',
    redirect: '/'
  }
]
