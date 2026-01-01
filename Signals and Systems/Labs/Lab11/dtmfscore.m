function sc = dtmfscore(xx, hh)
% DTMFSCORE
% usage: sc = dtmfscore(xx, hh)
% returns a score based on the max amplitude of the filtered output
% xx = input DTMF tone
% hh = impulse response of ONE bandpass filter
%
% The signal detection is done by scaling the input x[n] to the range [-2, +2],
% convolving it with the filter impulse response hh, and then checking if
% the maximum amplitude of the filtered output exceeds a threshold.
% The score is either 1 or 0.
% sc = 1 if max(abs(y[n])) is greater than or equal to 0.59
% sc = 0 if max(abs(y[n])) is less than 0.59
%
% Scale the input x[n] to the range [-2, +2]
xx = xx * (2 / max(abs(xx)));

% Convolve the input signal with the filter impulse response
yn = conv(xx, hh);
% Check if maximum amplitude of the filtered output exceeds threshold
if max(abs(yn)) >= 0.59
    sc = 1;
else
    sc = 0;
end
end