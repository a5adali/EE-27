function hn = dtmfdesign(fb, L, fs)
% DTMF Design Function
% Generates impulse and frequency responses for a set of frequencies using a bandpass filter design method.
%
% Inputs:
% - fb: Vector of center frequencies for the bandpass filters
% - L: Length of the FIR bandpass filters
% - fs: Sampling frequency of the signal
%
% Outputs:
% - hn: Matrix containing impulse responses of the filters

% Initialize variables to store impulse and frequency responses
hn = []; % Matrix to store impulse responses


n = 0:L - 1; % Time indices for the impulse responses
for i = 1:length(fb)
    % Calculate scaling factor using maxbeta function
    maxval = maxbeta(L, fb(i), fs);

    % Generate impulse response
    omg0 = 2 * pi * fb(i);
    impResponse = maxval * cos((omg0 * n) / fs);
    % Append impulse and frequency responses to matrices
    hn = [hn; impResponse];
end

% Transpose matrices for compatibility with typical usage
hn = hn';
end