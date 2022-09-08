const env = process.env;

export const nodeEvn = env.NODE_ENV || 'development';

export const logStars = function(message) {
    console.info('**********');
    console.info(message);
    console.info('**********');
};

export default {
    port: env.port || 8080
};