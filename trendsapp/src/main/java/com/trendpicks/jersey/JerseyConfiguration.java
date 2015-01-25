package com.trendpicks.jersey;

import java.util.logging.Logger;

import org.glassfish.jersey.filter.LoggingFilter;
import org.glassfish.jersey.server.ResourceConfig;
import org.glassfish.jersey.server.ServerProperties;
import org.glassfish.jersey.server.spring.scope.RequestContextFilter;
import org.springframework.stereotype.Component;

@Component
public class JerseyConfiguration extends ResourceConfig {

	private static boolean isLogEntity;
    private static Logger logger =  Logger.getLogger("JerseyConfiguration");

    public JerseyConfiguration() {
        packages("com.ehi.idm.rest");
        register(new LoggingFilter(logger, isLogEntity));
        register(RequestContextFilter.class);

        property(ServerProperties.TRACING, "ON_DEMAND");
        property(ServerProperties.BV_SEND_ERROR_IN_RESPONSE, true);
        property(ServerProperties.BV_DISABLE_VALIDATE_ON_EXECUTABLE_OVERRIDE_CHECK, true);
    }
    
}
