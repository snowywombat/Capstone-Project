import React, { useRef, useEffect } from 'react';

function VideoPlayer(props) {
  const playerRef = useRef(null);

  useEffect(() => {
    // Load the YouTube player API script
    const script = document.createElement('script');
    script.src = 'https://www.youtube.com/iframe_api';
    document.body.appendChild(script);

    // Initialize the YouTube player when the script is loaded
    script.onload = () => {
      new window.YT.Player(playerRef.current, {
        videoId: props.videoId,
        height: '360',
        width: '640',
        playerVars: {
          // https://developers.google.com/youtube/player_parameters
          autoplay: 1,
        },
      });
    };

    // Remove the script when the component unmounts
    return () => {
      document.body.removeChild(script);
    };
  }, [props.videoId]);

  return <div ref={playerRef} />;
}

export default VideoPlayer;
