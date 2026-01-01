% --- DTMF Dialer Function ---
function xx = dtmfdial(keyNames, fs)
    % DTMFDIAL Create a signal vector of tones which will dial
    % a DTMF (Touch Tone) telephone system.
    % 
    % usage: xx = dtmfdial(keyNames, fs)
    % keyNames = vector of characters containing valid key names
    % fs = sampling frequency
    % xx = signal vector that is the concatenation of DTMF tones.
    
    % Define the DTMF frequency table
    dtmf.keys = ['1','2','3','A';
                 '4','5','6','B';
                 '7','8','9','C';
                 '*','0','#','D'];
             
    dtmf.colTones = ones(4, 1) * [1209, 1336, 1477, 1633]; % Column frequencies
    dtmf.rowTones = [697; 770; 852; 941] * ones(1, 4); % Row frequencies
    
    % Duration specifications
    tone_duration = 0.20;  % 0.20 seconds per tone
    silence_duration = 0.05;  % 0.05 seconds silence
    t_tone = 0:1/fs:tone_duration-1/fs;  % Time vector for tone
    t_silence = zeros(1, floor(silence_duration * fs));  % Silence vector
    
    xx = [];  % Initialize the output signal
    
    % Loop through each key in the input keyNames
    for key = keyNames
        [row, col] = find(key == dtmf.keys);  % Find row and column indices
        
        % Check if the key is valid
        if isempty(row) || isempty(col)
            error('Invalid key: %s. Use 0-9, A-D, *, #.', key);
        end
        
        % Generate the two sinusoidal signals for the DTMF tone
        tone = cos(2 * pi * dtmf.rowTones(row, col) * t_tone) + ...
               cos(2 * pi * dtmf.colTones(row, col) * t_tone);
        
        % Concatenate the tone and silence
        xx = [xx, tone, t_silence];
    end
end