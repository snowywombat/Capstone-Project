import React from 'react';
import { useModal } from '../../context/Modal';
import '.././Navigation/Navigation.css';
import '.././Navigation/ProfileButton.css';



function OpenModalButtonAddRecipe({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose // optional: callback function that will be called once the modal is closed
}) {
  const { setModalContent, setOnModalClose } = useModal();

  const onClick = () => {
    if (onModalClose) setOnModalClose(onModalClose);
    setModalContent(modalComponent);
    if (onButtonClick) onButtonClick();
  };

  return (
    <>
    <button onClick={onClick} className='open-modal-button-recipes'>{buttonText}</button>
    </>
  );
}

export default OpenModalButtonAddRecipe;
