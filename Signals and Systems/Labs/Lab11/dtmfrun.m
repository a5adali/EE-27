function keys = dtmfrun(xx, L, fs)
% DTMF frequency table
dtmf.keys = ...
    ['1', '2', '3', 'A';
     '4', '5', '6', 'B';
     '7', '8', '9', 'C';
     '*', '0', '#', 'D'];

% Center frequencies for DTMF tones
dtmf.colTones = ones(4, 1) * [1209, 1336, 1477, 1633];
dtmf.rowTones = [697; 770; 852; 941] * ones(1, 4);

% Defines 1x8 vector of frequencies
center_freqs = [697, 770, 852, 941, 1209, 1336, 1477, 1633];
hh = dtmfdesign(center_freqs, L, fs);
% hh = L by 8 MATRIX of all the filters. Each column contains the
% impulse response of one BPF (bandpass filter)
% Find the beginning and end of tone bursts
[nstart, nstop] = dtmfcut(xx, fs);
% Initialize keys
keys = [];
% For each tone burst
for kk = 1:length(nstart)
    % Extract one DTMF tone
    xx_seg = xx(nstart(kk):nstop(kk));
    % Initialize score vector
    sc = zeros(1, 8);
    % Compute scores for each bandpass filter
    for i = 1:8
        sc(i) = dtmfscore(xx_seg, hh(:, i));
    end
    % Find indices of row and column tones with score 1
    r_ind = find(sc(1:4) == 1);
    c_ind = find(sc(5:8) == 1);
    % If both row and column tones are detected, append key to keys
    if length(c_ind) + length(r_ind) == 2
        keys = [keys dtmf.keys(r_ind, c_ind)];
    end 
end
end