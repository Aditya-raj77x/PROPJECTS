import React from 'react'

export default function Navbar() {
  return (
    <nav className='d-flex none'>
        <div className="nav_brand">
            <a href="/">
                <img src="./assets/logo.png" alt="" />
            </a>
        </div>
        <div className="search d flex">
            <input type="text" />
            <i className='fas fa search'></i>
        </div>
        <ul className='nav_menu d-flex'>
            <li>
                <a href="/">
                    Hello Guest <br />
                    <span>sign In</span>
                </a>

            </li>
            <li>
                <a href="/">
                    Return <br />
                    <span>Order</span>
                </a>
            </li>
            <li>
                <a href="/">
                    Your <br />
                    <span>Prime</span>

                </a>
            </li>
            <li>
                <a href="/">
                    <i className='fas fa-shopping cart'></i>
                </a>
            </li>
        </ul>

    </nav>
  )
}
