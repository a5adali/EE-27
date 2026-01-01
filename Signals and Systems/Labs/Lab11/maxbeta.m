function B = maxbeta(L, fb, fs)
    % Generate time vector
    n = 0:L-1;
    % Calculate angular frequency
    omg = 2 * pi * fb;
    % Generate impulse response of the filter
    x = cos(omg * n / fs);
    % Define frequency range for frequency response computation
    t = -pi:(pi/L):pi;
    % Compute frequency response of the filter
    hw = freqz(x, 1, t);
    maxval = max(abs(hw));
    B = 1 / maxval;
end