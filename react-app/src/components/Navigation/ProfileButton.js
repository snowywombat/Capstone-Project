import React, { useState, useEffect, useRef } from "react";
import { useHistory } from 'react-router-dom';
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import DemoFormModal from "../DemoModal";
import './ProfileButton.css'

function ProfileButton({ user }) {
  const history = useHistory();
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
    history.push('/')

  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);

  return (
    <>
      <button onClick={openMenu} className='profile-button'>
        MY ACCOUNT
      </button>
      <ul className={ulClassName} ref={ulRef}>
        {user ? (
          <>
            <li>{user.username}</li>
            <li>{user.email}</li>
            <li>
              <button className='logout-button' onClick={handleLogout}>Log Out</button>
            </li>
          </>
        ) : (
          <>
          <div className='dropdown-buttons'>
            <li>
              <OpenModalButton
                buttonText="Log In"
                onItemClick={closeMenu}
                className='open-modal-button'
                modalComponent={<LoginFormModal />}
              />
              </li>

              <li>
              <OpenModalButton
                buttonText="Sign Up"
                onItemClick={closeMenu}
                modalComponent={<SignupFormModal />}
              />
              </li>

              <li>
              <OpenModalButton
                buttonText="Demo"
                onButtonClick={closeMenu}
                modalComponent={<DemoFormModal />}
              />
            </li>
          </div>
          </>
        )}
      </ul>
    </>
  );
}

export default ProfileButton;
